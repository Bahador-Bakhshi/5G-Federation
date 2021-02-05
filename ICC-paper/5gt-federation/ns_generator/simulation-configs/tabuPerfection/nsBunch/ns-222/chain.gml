graph [
  node [
    id 0
    label 1
    disk 10
    cpu 3
    memory 6
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 1
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 12
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 9
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 3
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 174
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 114
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 99
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 81
  ]
  edge [
    source 2
    target 5
    delay 35
    bw 66
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 52
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 173
  ]
]
