graph [
  node [
    id 0
    label 1
    disk 2
    cpu 2
    memory 12
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 6
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 6
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 1
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 75
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 91
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 86
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 124
  ]
  edge [
    source 2
    target 4
    delay 35
    bw 151
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 156
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 170
  ]
]
