graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 2
    memory 11
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 13
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 117
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 65
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 174
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 94
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 124
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 103
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 52
  ]
]
