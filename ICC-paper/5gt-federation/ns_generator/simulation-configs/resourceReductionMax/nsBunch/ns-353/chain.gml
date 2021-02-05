graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 4
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 13
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 1
    memory 7
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 7
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 142
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 139
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 100
  ]
  edge [
    source 0
    target 3
    delay 33
    bw 180
  ]
  edge [
    source 1
    target 5
    delay 28
    bw 150
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 82
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 84
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 162
  ]
]
