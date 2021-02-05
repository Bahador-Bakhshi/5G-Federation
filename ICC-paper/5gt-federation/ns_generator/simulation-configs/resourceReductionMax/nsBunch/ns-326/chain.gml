graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 2
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 1
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 15
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 11
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 3
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 162
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 89
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 170
  ]
  edge [
    source 0
    target 3
    delay 28
    bw 80
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 66
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 53
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 125
  ]
]
