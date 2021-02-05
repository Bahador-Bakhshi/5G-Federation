graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 11
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 10
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 1
    memory 6
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 3
    memory 12
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 179
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 171
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 138
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 131
  ]
  edge [
    source 3
    target 4
    delay 34
    bw 90
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 159
  ]
]
