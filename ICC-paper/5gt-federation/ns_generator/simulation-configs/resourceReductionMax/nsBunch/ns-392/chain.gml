graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 16
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 14
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 1
    memory 2
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
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
    bw 187
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 200
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 162
  ]
  edge [
    source 0
    target 3
    delay 34
    bw 80
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 124
  ]
  edge [
    source 3
    target 5
    delay 26
    bw 97
  ]
]
