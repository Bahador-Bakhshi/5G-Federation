graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 10
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 4
    memory 15
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 9
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 4
    memory 14
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 81
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 110
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 132
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 103
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 78
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 139
  ]
  edge [
    source 3
    target 5
    delay 35
    bw 183
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 156
  ]
]
