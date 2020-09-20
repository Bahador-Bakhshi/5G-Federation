graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 7
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 6
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 11
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 4
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 157
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 164
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 191
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 139
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 59
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 84
  ]
]
