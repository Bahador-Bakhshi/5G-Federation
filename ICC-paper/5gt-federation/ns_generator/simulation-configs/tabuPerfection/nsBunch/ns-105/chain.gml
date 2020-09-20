graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 5
  ]
  node [
    id 1
    label 2
    disk 4
    cpu 1
    memory 2
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 9
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 8
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 5
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 2
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 139
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 96
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 138
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 199
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 164
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 95
  ]
]
